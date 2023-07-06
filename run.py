import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

from scrape import scrape


if __name__ == '__main__':

    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape, 'interval', seconds=10800)
    scheduler.start()
    print(f'Press Ctrll+{"Break" if os.name== "nt" else "C"} to exit')

    try:
        while True:
            time.sleep(10799)
    except:
        scheduler.shutdown()
