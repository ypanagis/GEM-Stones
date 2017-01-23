import logging
from argparse import ArgumentParser
from itertools import combinations
import subprocess

logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

courts = ["ecj", "echr"]
periods = ["earlier", "latest"]
INPUT_DIR = "../data/texts/{period}"
CORPUS = "../data/mallet/corpora/{period}-corpus.mallet"
#MODEL = "data/mallet/models/{court}-{period}-k{k}.model"
MALLET_PATH = r"C:\mallet\bin\mallet"



if __name__ == "__main__":

    for period in periods:
        input_path = INPUT_DIR.format(period=period)
        output_path = CORPUS.format(period=period)
        subprocess.call([MALLET_PATH, 'import-dir',
                         '--input', input_path,
                         '--output', output_path,
                         '--keep-sequence', '--remove-stopwords',
                         '--extra-stopwords', '../data/stopwords.en.txt'], shell='cmd')