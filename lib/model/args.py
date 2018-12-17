import os

from argparse import ArgumentParser

root_dir = os.getcwd()


def get_args():
    parser = ArgumentParser(description="Seq2Seq models for Neural Machine Translation (NMT)")
    parser.add_argument('--cpu', action='store_true')
    parser.add_argument('--devices', type=str, default='0,1')
    parser.add_argument('--ensemble', type=bool, default=False)
    parser.add_argument('--epochs', type=int, default=7)
    parser.add_argument('--batch-size', type=int, default=32)
    parser.add_argument('--hidden-dim', type=int, default=1000)
    parser.add_argument('--num-encoder-layers', type=int, default=2)
    parser.add_argument('--num-decoder-layers', type=int, default=2)
    parser.add_argument('--vocab-size', type=int, default=10000)
    parser.add_argument('--lr', type=float, default=0.7)
    parser.add_argument('--decay', type=float, default=0.5)
    parser.add_argument('--beam-size', type=int, default=2)
    parser.add_argument('--seed', type=int, default=3435)
    parser.add_argument('--dataset', type=str, default='en_vi', choices=['en_de', 'de_en', 'en_vi', 'vi_en'])
    parser.add_argument('--patience', type=int, default=5)
    parser.add_argument('--save-path', type=str, default='data/checkpoints')
    parser.add_argument('--embedding-dim', type=int, default=300)
    parser.add_argument('--embedding-path', help='embedding file path', default=os.path.join(root_dir, 'data', 'embeddings'))
    parser.add_argument('--dataset-path', help='dataset directory', default=os.path.join(root_dir, 'data', 'datasets'))
    parser.add_argument('--word-vectors-file', help='word vectors filename', default='GoogleNews-vectors-negative300.txt')
    parser.add_argument('--weight-decay', type=float, default=0)

    args = parser.parse_args()
    return args
