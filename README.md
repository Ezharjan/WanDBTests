# Learn WanDB

1. Install WanDB:
```bash
pip install wandb
```

2. Login via command line:
```bash
wandb.login()
```

3. Set WanDB based on the template codes shown in [`test.py`](./test.py)

4. Open [WanDB official web page](https://wandb.ai/) and login to your account to see the result.

5. [Reference](https://docs.wandb.ai/quickstart).

6. Example out is:
```bash
wandb: Currently logged in as: alexander-um. Use `wandb login --relogin` to force relogin
wandb: Appending key for api.wandb.ai to your netrc file: /home/alex/.netrc
wandb: Tracking run with wandb version 0.16.1
wandb: Run data is saved locally in /home/alex/Documents/WanDBTests/wandb/run-20231212_164426-7569wcec
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run my-test_12-12_16:44
wandb: ⭐️ View project at https://wandb.ai/alexander-um/my-test
wandb: 🚀 View run at https://wandb.ai/alexander-um/my-test/runs/7569wcec
wandb:                                                                                
wandb: 
wandb: Run history:
wandb:  acc ▁▄▄▆█▇█▇
wandb: loss █▅▅▃▁▁▃▂
wandb: 
wandb: Run summary:
wandb:  acc 0.81537
wandb: loss 0.18652
wandb: 
wandb: 🚀 View run my-test_12-12_16:44 at: https://wandb.ai/alexander-um/my-test/runs/7569wcec
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231212_164426-7569wcec/logs
```


7. The example output of the log result is [here](./log-result.png).