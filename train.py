import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import pickle

# Load dataset
data = open("dataset.txt").read()

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])

total_words = len(tokenizer.word_index) + 1

# Create input sequences
input_sequences = []

for line in data.split('\n'):

    token_list = tokenizer.texts_to_sequences([line])[0]

    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

# Pad sequences
max_sequence_len = max([len(x) for x in input_sequences])

input_sequences = np.array(
    pad_sequences(
        input_sequences,
        maxlen=max_sequence_len,
        padding='pre'
    )
)

# Split predictors and labels
X = input_sequences[:, :-1]
y = input_sequences[:, -1]

# Build model
model = Sequential()

model.add(
    Embedding(
        total_words,
        10,
        input_length=max_sequence_len - 1
    )
)

model.add(LSTM(100))

model.add(
    Dense(
        total_words,
        activation='softmax'
    )
)

# Compile model
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Train model
model.fit(X, y, epochs=200, verbose=1)

# Save model
model.save("model.h5")

# Save tokenizer
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("Training Completed Successfully!")