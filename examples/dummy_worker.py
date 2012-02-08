import os
import signal
import sys
import time


class DummyWorker(object):

    def __init__(self, wid):
        self.wid = wid
        # init signal handling
        signal.signal(signal.SIGQUIT, self.handle_quit)
        signal.signal(signal.SIGTERM, self.handle_quit)
        signal.signal(signal.SIGINT, self.handle_quit)
        signal.signal(signal.SIGCHLD, self.handle_chld)
        self.alive = True

    def handle_quit(self, *args):
        self.alive = False
        sys.exit(0)

    def handle_chld(self, *args):
        return

    def run(self):
        print "hello, worker #%s (pid: %s) is alive" % (self.wid, os.getpid())

        while self.alive:
            time.sleep(0.1)

if __name__ == "__main__":
    DummyWorker(sys.argv[1]).run()
