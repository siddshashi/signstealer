# Baseball Sign Stealer

Right now, I'm trying to write a bot to interpret a diverse array of sequences and map them to more than 2 plays. I also want to look into other forms of signals like wipe-offs and frequency as an input. Once I'm done with college applications, I'll be sure to get on it. So far, I've done the following: 

Generated a dataset that maps a sequence of letters (gesture = letter) to a 0 or 1 (0 = no steal, 1 = steal). You will find these in the h1k and h10k files. 

Created an initializer that tells the neural net how to interpret the data. This is the init.py file. 

Created a training file that trains the neural net with the dataset you give. This is the train.py file. Usually, the way to get better predictions is to train with the larger file (h10k) and then predict with the smaller file (h1k). 

Created a predicting file that uses the trained net to predict the outputs for any new dataset given. This is the predict.py file. 

Finally, I wrote a file to put everything together and call each program. This is the hub.py file. 
