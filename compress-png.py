import os

base_path = '.'

for dirname, dirnames, filenames in os.walk(base_path):

    for filename in filenames:

        if '.png' in filename:
            print 'comprimindo %s' % filename 
            command = 'pngquant -f -ext .png 128 %s/%s' % (dirname, filename)
            # print command
            os.system(command)