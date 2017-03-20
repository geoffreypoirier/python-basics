import sys

sys.stderr.write('stderr text\n')
sys.stderr.flush()
sys.stdout.write('stdout text\n')


print(sys.argv)

if len(sys.argv) > 1:
	for argCounter in range(len(sys.argv)):
		print(argCounter, sys.argv[argCounter])
		pass