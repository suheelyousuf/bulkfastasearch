---
title: 'BulkFastaSearch: A GUI based tool for extracting multiple sequences using their ids (.txt) from a bigger file (.fasta, fasta.gz) altogether'
tags:  
  - Python
  - Algorithm
  - genomics
  - genome
authors:
  - name: Mohanad A. Ibrahim 
    orcid: 0000-0000-0000-0000
    affiliation: 1
  - name: Suheel Yousuf Wani
    orcid: 0000-0002-3793-3504
    affiliation: 1
  affiliations:
  - name: Department of Genome, Ministry of Environment Water & Agriculture, Riyadh, KSA
    index: 1
date: 25 July 2022  
bibliography: paper.bib
---

# Summary
NGS analyses involve the basic manipulation of input sequence data before downstream processing (e.g. searching for specific sequences). The rapidly increasing data volumes involved in NGS make any dataset manipulation a time-consuming and error-prone process. And also extracting subset of reads manually from large fasta files becomes inpractical and time consuming. To automate this process overcome this problem, we have developed BulkFastaSearch which is a GUI based software tool with good usability and is written in python.
# Statement of need
BluckFastaSearch extracts Magphi extracts genomic regions of interest from FASTA and Gene Feature Format 3 (GFF3) files, both being common file types in bioinformatics. Packages such as Seqkit [@shen:2016] allow for extraction and manipulation of FASTA and FASTQ files; However, such tools do not work with GFF3, or when regions of interest may span across contigs. Handling of GFF3 files are often necessary when researchers examine annotated genomes, as these are not included in FASTA formatted files.  

BluckFastSearch is a GUI tool written in Python 3 and GUI is created through tkinter. Tkinter is python interface to Tcl/tk.   

BluckFastSearch is scalable and can take multiple genomes and pairs of seed sequences. Outputs are divided by the input seed sequences for easier file management.

# Acknowledgements
This work is supported by Ministry of Ministry of Environment Water & Agriculture, Riyadh, KSA .

# References
