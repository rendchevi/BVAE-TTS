from text import symbols


################################
# Experiment Parameters        #
################################
seed=1234
output_directory = 'DEV/checkpoints/TITML-IDN-F01'
iters_per_validation=250
iters_per_checkpoint=1000

data_path = 'DEV/datasets/TITML-IDN-F01-22kHz/preprocess_melTAC_phonEN'
training_files='DEV/filelists/TITML-IDN-F01-trainfiles.txt'
validation_files='DEV/filelists/TITML-IDN-F01-valfiles.txt'
test_files='DEV/filelists/TITML-IDN-F01-valfiles.txt'
text_cleaners=['english_cleaners']


################################
# Audio Parameters             #
################################
sampling_rate=22050
filter_length=1024
hop_length=256
win_length=1024
n_mel_channels=80
mel_fmin=0
mel_fmax=8000.0


################################
# Model Parameters             #
################################
n_symbols=len(symbols)
data_type='phone_seq'
n_blocks=4
n_layers=3
kernel_size=5
downsample_ratio=4
symbols_embedding_dim=256
hidden_dim=256
max_db=2
min_db=-12


################################
# Optimization Hyperparameters #
################################
lr=1e-3
lr_warmup_steps=4000
kl_warmup_steps=60000
grad_clip_thresh=1.0
batch_size=4
train_steps=10000 #300000

