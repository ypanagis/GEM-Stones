import logging
from argparse import ArgumentParser
from itertools import combinations
import subprocess

logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

periods = ["earlier", "latest"]
INPUT_DIR = "../data/texts/{period}"
# The output directory for the corpus files. Make sure the direcotyr exists
CORPUS = "../data/mallet/corpora/{period}-corpus.mallet"
MODEL = "../data/mallet/models/{period}-{k}.mallet"
MALLET_PATH = r"C:\mallet\bin\mallet"


if __name__ == "__main__":
    for period in periods:
        # Fix a value of k. We can obviously have different values of k
        k = 20
        input_path = CORPUS.format(period=period)
        output_path = MODEL.format(period=period, k=k)
        print output_path
        res = subprocess.call([MALLET_PATH, 'train-topics',
                         '--input', input_path,
                         '--num-topics', str(k),
                         '--num-iterations', '1000',
                         '--num-threads', '1',
                         '--optimize-interval', '5',
                         '--output-state', output_path + '.model.state.gz',
                         '--output-model', output_path + '.model',
                         '--output-doc-topics', output_path + '-doc-topics.txt',
                         '--output-topic-keys', output_path + '-topic-keys.txt',
                         # '--output-topic-docs', output_path + '-topic-docs.txt',
                         '--alpha', '1',
                         '--random-seed', '1',
                         '--word-topic-counts-file', output_path + '-word-topic-counts.txt',
                         '--topic-word-weights-file', output_path + '-topic-word-weights.txt',

                         ], shell=True)