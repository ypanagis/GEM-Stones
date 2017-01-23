# GEM-Stones
A repository for the lecture in CBS, for the GEM-Stones methods workshop

# Introduction
This is a repository created for the lecture _Text as Data I_ carried out for the _GEM-Stones Methods Workshop_ on January 27, 2017 at the Copenhagen Business School

# Presentation
The presentation is [here](Panagis-Texts as data.pptx)

## Structure
 * [data](data): contains data for the workshop
   * [texts](texts): contains text data that will be used. Two folders `earlier`and `latest` have judgments from ECHR. `corpus.echr.200.gz` are some data saved from R and `echr.200.tsv` are 200 judgments from ECHR randomly selected from the period 2005-2015
   * [mallet](mallet): is used for reading and writing data for **MALLET**.
   * `celex.txt`: Contains URLs for 16 judgments of the _Court of Justice of the EU_.
   * `Judgment Appl.001-2008 Michelot Yogogombaye v Senegal- English.pdf`: Example of a judgment that is scanned. The `.txt` file with the same name is the OCRed text, with many OCR error
   * `stopwords.en.txt`: a list of common [stop-words](https://en.wikipedia.org/wiki/Stop_words) in English with some court-specific words added
   
 * [notebooks](notebooks): An R notebook with a demo of [Structural Topic Modeling](http://structuraltopicmodel.com)
 * [scripts](scripts): Python scripts to use MALLET, more on the [Scripts](#scripts) session
 * [utilities](utilities): 
   * **AntConc**: for Windows x64 (.exe) and for Mac (.zip)
   * **Mallet**: the 2.0.7 version of the software. Simply unzip. In windows you have to create a `MALLET_HOME` environment variable
   * **Tika**: The 1.14 version of Apache Tika (`tika-app-1.14.jar`). Need Java to run

## Scripts
The scripts are Python 2.7 scripts to use Mallet. Both scripts work with the texts in the folder [texts](texts). 
### Prerequisites
You need to have Python 2.7 installed in your system and MALLET installed in `C:\mallet`. Otherwise modify `MALLET_PATH` in both .py files to your actual MALLET installation
### Description
`mallet-import` reads the files from [data/texts](data/texts) both `earlier` and `latest` subdirectories and contructs corresponding corpora saved in `data/mallet/corpora`, one corpus per directory. To execute the script, open and terminal and write:
```
python mallet-import.py
```
`mallet-train` reads the the corpora constructed with the `mallet-import` command and trains two models with `K=20` topics each, for both periods. The models are written in `data/mallet/models`. 

**Files of interest:**
 * `[period]-20.mallet-doc-topics.txt` are the document topics probabilities
 * `[period]-20.mallet-topic-keys.txt` are the most common words for each of the 20 topics
 * `[period]-20.mallet-topic-word-weights.txt` are the topic word probabilities
 
**Execution:** Open a terminal and write
```
python mallet-train.py
```

## Author
_Yannis Panagis_ `<ioannis.panagis (at) jur (dot) ku (dot) dk>` [iCourts](http://jura.ku.dk/icourts/staff)
