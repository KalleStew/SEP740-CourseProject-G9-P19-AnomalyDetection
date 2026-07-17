from model import Autoencoder

model  = Autoencoder (input_dim = X_train.shape[1], latent_dim = 16)
model.compile(optimizer = 'adam', loss = 'mse')
model.fit(
    X_train,
    X_train,
    epochs=50,
    batch_size=256
)