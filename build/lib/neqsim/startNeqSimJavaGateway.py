import os
from os import path
import pkg_resources
resources_dir = pkg_resources.resource_filename('neqsim', 'lib/')
fullstring = 'java -classpath '+resources_dir+'/NeqSimpy4j.jar;'+resources_dir+'/NeqSimSource.jar;'+resources_dir+'/py4j0.10.8.1.jar neqsimpy4j.startJavaGateway'
print(fullstring)
os.system(fullstring)
print("started neqsim Java Gateway...")