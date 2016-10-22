import os

my_path = os.path.join(os.path.split(os.path.dirname(os.path.realpath(__file__)))[:-1])[0]
destination = os.path.expanduser('~')

def link():
    target_paths = get_target_paths()
    from_dir = destination

    symlinks = {}
    for target_path in target_paths:
        to_directory, to_filename = os.path.split(target_path)
        from_filename = to_filename

        from_path = os.path.join(from_dir,from_filename)        
        symlinks[from_path] = target_path

    # Attempt to create the symlinks that don't already exist.
    for from_path,target_path in symlinks.items():                        
        # Check that nothing already exists at from_path.
        if os.path.islink(from_path):
            # A link already exists.
            existing_target_path = os.readlink(from_path)
            existing_target_path = os.path.abspath(os.path.expanduser(existing_target_path))
            if  existing_target_path == target_path:
                # It's already a link to the intended target. All is
                # well.
                continue
            else:
                # It's a link to somewhere else.
                print from_path+" => is already symlinked to "+existing_target_path
        elif os.path.isfile(from_path):
            print "There's a file in the way at "+from_path
        elif os.path.isdir(from_path):
            print "There's a directory in the way at "+from_path
        elif os.path.ismount(from_path):
            print "There's a mount point in the way at "+from_path
        else:
	    print 'Making symlink %s->%s' % (from_path,target_path)
	    os.symlink(target_path,from_path)


def get_target_paths(target_dir=my_path,report=False):
    """Return the list of absolute paths to link to for a given target_dir.
    
    This handles skipping various types of filename in target_dir and
    resolving host-specific filenames.
    
    """
    paths = []
    filenames = os.listdir(target_dir)
    for filename in filenames:
        path = os.path.join(target_dir,filename)
        if filename.endswith('~'):
            if report:
                print 'Skipping %s' % filename
            continue            
        elif (not os.path.isfile(path)) and (not os.path.isdir(path)):
            if report:
                print 'Skipping %s (not a file or directory)' % filename
            continue
        elif not(filename.startswith('.')):
            if report:
                print 'Skipping %s (filename has no leading dot)' % filename
            continue
        else:
	    paths.append(path)    
    return paths

if '__main__' == __name__:
    link()
