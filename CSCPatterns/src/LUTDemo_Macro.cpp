/*
 * comparatorCodeEmulator.cpp
 *
 *  Created on: Apr 27, 2018
 *      Author: williamnash
 */

#include "../include/CSCHelperFunctions.h"
#include "../include/LUTClasses.h"
#include <TGraph.h>
#include <TF1.h>
#include <TSystem.h>
#include <TH1F.h>

//c++
#include <fstream>
#include <math.h>

using namespace std;


int LUTDemo_Macro(){
	gSystem->Load("../lib/CSCClasses_cpp.so");
	gSystem->Load("../lib/LUTClasses_cpp.so");
	gSystem->Load("../lib/CSCHelperFunctions_cpp.so");

	//all the patterns we will fit
	vector<CSCPattern>* newPatterns = createNewPatterns();

	//output file stream to write the fits
	const string lutName = "../dat/linearFits.lut";

	LUT* lut = new LUT();
	lut->loadText(lutName);
	lut->print();
	lut->makeFinal();
	//key into the look up table with pattern id / comparator code
	unsigned int patternId        = 100;
	unsigned int comparatorCodeId = 10;

	std::cout << "Looking for Pattern Id: " << patternId << " Comparator Code: " << comparatorCodeId << std::endl;

	LUTKey key(patternId,comparatorCodeId);

	//create a new null pointer to an entry that is set by the LUT
	const LUTEntry* entry = 0;

	lut->getEntry(key, entry);

	if (!entry){
		std::cout << "No entry in look up table" << std::endl;
	} else {
		std::cout<< "LUT position is: " << entry->position() << std::endl;
	}

	return 0;
}

