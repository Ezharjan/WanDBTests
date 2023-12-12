import time
import wandb
import random

wandb.login(key="ba6e30d9de6bd4ce17968e79eb915c2226708add") # directly login via code, must match with real account password!!!

# set wandb initial information
run_time = time.strftime("%m-%d_%H:%M", time.localtime())
experiment_name = (
    "my-test" + "_" + run_time
)

# start a new wandb run to track this script
wandb.init(
    # set the wandb project where this run will be logged
    project="my-test", # name of the project
    name=experiment_name, # name of the experiment in this run
    entity="alexander-um", # account name must be corespondent to the registered account name on WanDB!!!
)

# simulate training
epochs = 10
offset = random.random() / 5
for epoch in range(2, epochs):
    acc = 1 - 2**-epoch - random.random() / epoch - offset
    loss = 2**-epoch + random.random() / epoch + offset

########################################################################
    # log metrics to wandb
    wandb.log({"acc": acc, "loss": loss}) # set log here via this line
########################################################################


# [optional] finish the wandb run, necessary in notebooks
wandb.finish()
