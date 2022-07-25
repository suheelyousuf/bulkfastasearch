# BluckFastaSearch
**Tool intended to pull out or extract multipul sequences from a large fasta file by providing sequence ids**

## When to use
If you have a large fasta file (.fasta or .fasta.gz) and you want to search or extract multiple sequences from this file on the basis of sequence ids.
This tool is particularly useful to the pure biologits who don't have knowledge to write scripts as this tool comes with a GUI. 
This tool is more useful if there is text file containg the sequnce ids seprated by commas, you just need to upload that text file in the tool and the all the sequences with these sequences ids get extracted and a seprate fasta file will be created, that will contain only those sequences whose sequence ids are metioned in the input text file.

## Home Screen 
![Home Screen](https://github.com/suheelyousuf/bulkfastasearch/blob/master/Home-Screen.png)

## Installation
### To run the tool
``` python Bulksearch.py ```


#### Dependencies
* Python >= 3.6
* Biopython
* tkinter
