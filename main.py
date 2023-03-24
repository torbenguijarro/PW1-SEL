import argparse
from preprocess import preprocess_iris


parser = argparse.ArgumentParser()

### run--> python3 main.py --dataset vote
parser.add_argument("--dataset", type=str, default='iris', choices=['iris'])

con = parser.parse_args()



def configuration():
    config = {
                'dataset':con.dataset,
             }
    return config









def main():
    config = configuration()



    if config['dataset'] == 'iris':
        X, Y = preprocess_iris()
















if __name__ == '__main__':
    main()












