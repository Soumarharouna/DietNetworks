import os

from featsel_supervised import execute


def main(embedding_path, which_method="pca"):

    print "Starting main loop"
    embedding_methods = []

    print "Method: {}".format(which_method)

    embedding_methods = os.listdir(embedding_path)
    embedding_methods = [emb for emb in embedding_methods
                         if ".npz" in emb and which_method in emb]

    if which_method == "kmeans":
        embedding_methods = [emb for emb in embedding_methods if
                             "hard" in emb]

    print "Embedding methods: {}".format(embedding_methods)
    mod = 1
    lr_candidates = [1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]

    for lr_value in lr_candidates:
        for embedding in embedding_methods:
            print "Training model %s: lr %d out of %d" % \
                    (embedding, mod, len(lr_candidates))
            execute(embedding, num_epochs=1000, split_valid=.2,
                    lr_value=lr_value,
                    save_path=embedding_path)
        mod += 1

if __name__ == '__main__':

    # embedding_path = "/data/lisatmp4/sylvaint/data/feature_selection/"
    embedding_path = "/data/lisatmp4/romerosa/feature_selection/"
    main(embedding_path, "kmeans")
