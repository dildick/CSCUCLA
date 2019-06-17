/*
 * PatternFitter.h
 *
 *  Created on: Oct 9, 2017
 *      Author: williamnash
 */

#ifndef PATTERNFITTER_H_
#define PATTERNFITTER_H_

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <string>
#include <iomanip>

//lambda
#include <functional>

#include "PatternConstants.h"
#include "../include/LUTClasses.h"
#include "../include/CSCInfo.h"

using namespace std;

/* @brief With clever scheme here:
 *
 * https://indico.cern.ch/event/712513/contributions/2959915/attachments/1630667/2599369/20180410_otmb_pattern_logic.pdf
 *
 * Can encode "comparator codes" within patterns.
 *
 */
class ComparatorCode {
public:
	ComparatorCode(bool hits[NLAYERS][3]);
	ComparatorCode(const ComparatorCode& c);
	ComparatorCode();

	~ComparatorCode() {}

	bool _hits[NLAYERS][3]; //all the hits within a pattern that a chamber scan matched

	unsigned int getLayersMatched() const;
	int getId() const;
	void printCode() const;
	static string getStringInBase4(int code);

private:
	int _id;
	int _layersMatched;

	void calculateId();
	void calculateLayersMatched();
};




/* @brief CSCPattern is a pattern used by the TMB as a first pass
 * towards creating a CLCT. Each have an acceptance for numerous tracks,
 * but give rough information as to the tracks slope.
 *
 * Comparator codes are created out of hits within a pattern.
 */
class CSCPattern {
public:
	CSCPattern(unsigned int id, bool isLegacy, const bool pat_[MAX_PATTERN_WIDTH][NLAYERS]);
	CSCPattern(string name, unsigned int id, bool isLegacy, const bool pat[MAX_PATTERN_WIDTH][NLAYERS]);
	CSCPattern(const CSCPattern &obj);
	CSCPattern();

	~CSCPattern() {}

	const unsigned int _id;
	const bool _isLegacy;
	bool _pat[MAX_PATTERN_WIDTH][NLAYERS];

	CSCPattern makeFlipped(unsigned int id) const;
	CSCPattern makeFlipped(string name, unsigned int id) const;
	void printCode(int code) const;
	int recoverPatternCCCombination(int code, int code_hits[MAX_PATTERN_WIDTH][NLAYERS]) const;
	string getName() const;

private:
	string _name;
};


/* @brief A candidate "road" within the CSC chamber made of a series
 * of hits compressed into a comparator code
 */
class CLCTCandidate {
public:
	CLCTCandidate(CSCPattern p, int horInd, int startTime, bool hits[NLAYERS][3]);
	CLCTCandidate(CSCPattern p, int horInd, int startTime, int layMatCount);

	~CLCTCandidate();

	const CSCPattern _pattern;
	const int _horizontalIndex; //half strips, leftmost index of the pattern
	const int _startTime;
	//pointer to whatever LUT Entry is associated with this candidate
	const LUTEntry* _lutEntry;

	int getHits(int code_hits[MAX_PATTERN_WIDTH][NLAYERS]) const;
	float keyStrip() const;
	int keyHalfStrip() const;
	float position() const;
	float slope() const;
	void print3x6Pattern() const;
	void printCodeInPattern() const;
	int comparatorCodeId() const;
	int layerCount() const;
	const ComparatorCode getComparatorCode() const;
	int patternId() const;
	const LUTKey key() const;

	//declare a function pointer used to sort the CLCT Candidates
	typedef function<bool(CLCTCandidate*, CLCTCandidate*)> QUALITY_SORT;
	static QUALITY_SORT quality;

private:
	ComparatorCode* _code;
	int _layerMatchCount;
	//float _quality;

};

class CLCTCandidateCollection
{
	public:
	
	std::vector<int> _horizontalIndex;
	std::vector<int> _startTime;	
	std::vector<float> keyStrip;
	std::vector<int> keyHalfStrip;
	std::vector<int> comparatorCodeId;
	std::vector<int> layerCount;
	std::vector<int> patternId;	
	std::vector<int> ch_id;	

	CLCTCandidateCollection(TTree *t, int i)
	{	
		if(i==1)
		{
			t->Branch("OP_horizontalIndex", &_horizontalIndex);
			t->Branch("OP_startTime", &_startTime);			
			t->Branch("OPKeyStrip", &keyStrip);
			t->Branch("OPKeyHalfStrip", &keyHalfStrip);		
			t->Branch("OPcomparatorCodeId", &comparatorCodeId);
			t->Branch("OPlayerCount", &layerCount);
			t->Branch("OPpatternId", &patternId);		
			t->Branch("OPch_id", &ch_id);	
		}	
				
		if(i==2)
		{
			t->Branch("NP_horizontalIndex", &_horizontalIndex);
			t->Branch("NP_startTime", &_startTime);			
			t->Branch("NPKeyStrip", &keyStrip);
			t->Branch("NPKeyHalfStrip", &keyHalfStrip);		
			t->Branch("NPcomparatorCodeId", &comparatorCodeId);
			t->Branch("NPlayerCount", &layerCount);
			t->Branch("NPpatternId", &patternId);		
			t->Branch("NPch_id", &ch_id);	
		}
	}	

	void Fill(vector<CLCTCandidate*> emulatedCLCTs, unsigned int chamberHash);	
	void Erase();
	//void FillTree(TTree* t);
};

class EmulatedCLCTs 
{
	public:

	EmulatedCLCTs() 
	{	
		
		_horizontalIndex = 0;
		_startTime = 0;		
		keyStrip = 0;
		keyHalfStrip = 0;	
		comparatorCodeId = 0;
		layerCount = 0;
		patternId = 0;		
		ch_id = 0;
	}

	EmulatedCLCTs(TTree* t) : EmulatedCLCTs()
	{		
		t->SetBranchAddress("_horizontalIndex", &_horizontalIndex);
		t->SetBranchAddress("_startTime", &_startTime);		
		t->SetBranchAddress("KeyStrip", &keyStrip);
		t->SetBranchAddress("KeyHalfStrip", &keyHalfStrip);		
		t->SetBranchAddress("comparatorCodeId", &comparatorCodeId);
		t->SetBranchAddress("layerCount", &layerCount);
		t->SetBranchAddress("patternId", &patternId);		
		t->SetBranchAddress("ch_id", &ch_id);
	}

	unsigned int size() const 
	{
		return ch_id ? ch_id->size() : 0;
	}

	unsigned int size(int chamber_index) const 
	{
		if(!ch_id) return 0;
		unsigned int count =0;
		for(auto id : *ch_id)
		{
			if(chamber_index == id) count++;
		}
		return count;
	}
	
	std::vector<int>* _horizontalIndex;
	std::vector<int>* _startTime;		
	std::vector<float>* keyStrip;
	std::vector<int>* keyHalfStrip;
	std::vector<int>* comparatorCodeId;
	std::vector<int>* layerCount;
	std::vector<int>* patternId;	
	std::vector<int>* ch_id;

};

/* @brief Encapsulates hit information for recorded event
 * in a chamber, identified by its station, ring, endcap and chamber
 */
class ChamberHits {
public:
	ChamberHits(unsigned int station, unsigned int ring,
			unsigned int endcap, unsigned int chamber, bool isComparator=true);
	ChamberHits(const ChamberHits& c);

	~ChamberHits(){}

	const bool _isComparator;
	const unsigned int _station;
	const unsigned int _ring;
	const unsigned int _endcap;
	const unsigned int _chamber;
	unsigned int minHs() const {return _minHs;}
	unsigned int maxHs() const {return _maxHs;}
	unsigned int nhits() const {return _nhits;}
	float hitMeanHS();
	float hitStdHS();
	int _hits[N_MAX_HALF_STRIPS][NLAYERS];

	bool shift(unsigned int lay) const;

	int fill(const CSCInfo::Comparators& c);
	int fill(const CSCInfo::RecHits& r);
	void print() const; //deprecated
	friend ostream& operator<<(ostream& os, const ChamberHits& c);

	ChamberHits& operator-=(const CLCTCandidate& mi);
private:
	unsigned int _nhits;
	unsigned int _minHs;
	unsigned int _maxHs;

	float _meanHS;
	float _stdHS;

};




#endif /* PATTERNFITTER_H_ */
