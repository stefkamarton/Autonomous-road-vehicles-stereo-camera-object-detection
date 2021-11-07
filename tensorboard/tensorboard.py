from tensorboard import program
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Read Tensorflow log files')
    parser.add_argument('--logdir', dest='logdir',help='logger directory', default="logs/", type=str)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    tboard = program.TensorBoard()
    tboard.configure(argv=[None, '--logdir', args.logdir])
    url = tboard.launch()
    tboard.main()
    print(f"Tensorflow listening on {url}")