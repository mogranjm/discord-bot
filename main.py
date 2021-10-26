# Dependency imports
import multiprocessing

for bot in ('dankmemerSend', 'dankmemerReact'):
	p = multiprocessing.Process(target=lambda: __import__(bot) )
	p.start()
