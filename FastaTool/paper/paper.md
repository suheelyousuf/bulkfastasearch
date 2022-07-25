---
title: 'BulkFastaSearch: A GUI based tool for extracting multiple sequences using their ids (.txt) from a bigger file (.fasta, fasta.gz) altogether'
tags:  
  - Python
  - Algorithm
  - genomics
  - genome
authors:
  - name: Mohanad A. Ibrahim 
    orcid: 0000-0002-8282-6169
    affiliation: 1
  - name: Suheel Yousuf Wani
    orcid: 0000-0002-3793-3504
    affiliation: 1
  - name: Fasil Al
    affiliation: 1
  affiliations:
  - name: Department of Genome, Ministry of Environment Water & Agriculture, Riyadh, KSA
    index: 1
date: 25 July 2022  
bibliography: paper.bib
---

# Summary
NGS analyses involve the basic manipulation of input sequence data before downstream processing (e.g. searching for specific sequences). The rapidly increasing data volumes involved in NGS make any dataset manipulation a time-consuming and error-prone process. And also extracting subset of sequences manually from large fasta files becomes inpractical and time consuming. To automate this process and to overcome this problem, we have developed BulkFastaSearch which is a GUI based software tool with good usability and is written in python.
# Statement of need
Programming languages like Python and Perl can be used to manipulate and modify the FASTA files. However, it is hard for medical scientists and pure biologists to write scripts for these standard tasks like extracting sequences using an IDs list file. And also the majority of tools developed till date for the fasta files manipulation are very hard to install and all of these available tools has command-line interface (CLI). Tools like Fasta utilities [@Hester J:2017], fastx toolkit [@Hanonlab.:2018], pyfaidx [@Shirley MD, Ma Z, Pedersen BS, Wheelan SJ : 2016], seqmagick [@2014], and seqtk [@2015] are just a few of the many tools that may be used to manipulate FASTA files but non of these tools has graphical user interface(GUI). The majority of these applications, however, do not handle huge compressed fasta files.

BluckFastSearch is a GUI tool written in Python 3 and GUI is created through tkinter. Tkinter is python interface to Tcl/tk.   

BluckFastSearch is scalable and can take Fasta (.gz) files as inputs . Outputs are stored in another fasta file where user has to provide the name of the result file.

# Acknowledgements
This work is supported by Ministry of Ministry of Environment Water & Agriculture, Riyadh, KSA .

# References
