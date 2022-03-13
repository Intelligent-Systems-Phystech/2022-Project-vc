# Folder with code

- data.py -- initial data stored as json files. This script converts the columns of interest to us in a tabular (pandas.DataFrame) format.

Prefix `data` -- scripts work with data in the first line of data process.

- data-embeddings.ipynb -- I use `cointegrated/LaBSE-en-ru` transformer for generate embeddings corresponding to education field of study field in LinkedIn profile.

Prefix `prep` -- scripts work with data in the first line of data process.

- prep-clustering.ipynb -- visualization of `cointegrated/LaBSE-en-ru` generated embeddings.
- prep-sentence-similarity.ipynb -- classification of education field of study field in LinkedIn profile using `sentence-transformers/multi-qa-MiniLM-L6-cos-v1`.
