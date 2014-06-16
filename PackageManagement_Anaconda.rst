Package Management
==================

We recommend using anaconda-python, since it is the most feature-rich and
science-friendly package manager.  It includes astropy, which few others do.

First, download the appropriate installer from the `continuum.io download page
<http://continuum.io/downloads>`_::

    wget http://......./Anaconda-1.9.2-MacOSX-x86_64.sh

Then run the command::

    sh Anaconda-1.9.2-MacOSX-x86_64.sh

and follow the instructions.  You will need to add the conda executable path,
probably ``~/anaconda/bin``, to your path in ``.bashrc`` or ``.login`` or
whatever you use as a startup file.

Once you've done this, you can use anaconda as a simple package manager::

    conda install astropy

You can update packages to their latest versions with one command::

    conda update conda

You can also pip install things as usual, and use ``python setup.py install``
as usual.

For more details, visit the `anaconda introduction page
<http://conda.pydata.org/docs/intro.html>`_.

Packaged Python Distributions
-----------------------------

`Enthought <https://www.enthought.com/products/epd/>`_ distributes a product
including matplotlib and numpy.

`Scipy Superpack <http://fonnesbeck.github.io/ScipySuperpack/>`_ is
mac-specific and requires the latest Xcode, but will install up-to-date scipy,
numpy, and matplotlib.

Python Versions
---------------

You should use python >= 2.7.6.  Python 2.6 is still usable in many cases, but
has some missing syntax.  Older versions, python 2.5 and earlier, can sometimes
be found on old servers - these are effectively unusable.

Python 3.3 and 3.4 can be used for many scientific applications now, but not
all packages support python 3.

Compilers
---------
You need a compiler to install many astronomy-related packages from source, and
you should have one in general.

If you are frequently compiling the same source code, i.e. if you are working on
developing a C package with many dependencies that need recompiling, `ccache
<ccache.samba.org/manual.html>`_ is useful for boosting speed.


Other Installers
----------------

`easy_install <http://pythonhosted.org/setuptools/easy_install.html>`_ is the outdated
way to install packages from `the python package index <pypi.python.org>`_.

`pip <https://pypi.python.org/pypi/pip>`_ is the `preferred
<http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install>`_.
It will install any packages indexed on `the python package index`_, and it can
install anything with an associated URL.

For example, one can install any package that has an appropriate ``setup.py`` (etc.)
and is hosted on `github <github.com>`_ or `bitbucket <bitbucket.org>`_:

    pip install https://github.com/keflavich/FITS_tools/archive/master.zip

or, assuming you have `git <http://git-scm.com/>`_ installed:

    pip install -e git+git@github.com:keflavich/FITS_tools.git#egg=FITS_tools

Don't use ``sudo easy_install [packagename]``.  If you hit that situation, you
are better off switching to either conda or `virtualenv
<http://virtualenv.readthedocs.org/en/latest/>`_.

Virtualenv
----------
If you don't have ``sudo`` priveleges on your machine, you can still use
virtualenv.

    $ curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-X.X.tar.gz
    $ tar xvfz virtualenv-X.X.tar.gz
    $ cd virtualenv-X.X
    $ python virtualenv.py myVE

After you have created a virtualenv, you can "activate" it (putting the
virtualenv's python first on your path) with the provided activate script:

    $ source bin/activate

Using bleeding-edge software & developing
-----------------------------------------
If you're using code more recent than the latest release or code that you want
to frequently update, the best option is often to ``clone`` the source code
repository and use ``python setup.py develop`` to keep it perpetually up to
date.  *However,* this approach will not keep compiled C and FORTRAN code up to
date!

``python setup.py develop`` creates a set of symbolic links from the source
code directory to the python environment directory.

Package Management within CASA
------------------------------
CASA comes with a fully functional python stack, including matplotlib & numpy.
However, its ``python`` executable is not easily accessible and the normal CASA
python path is often overwritten.  There is a wrapper script called
`casa-python <https://github.com/radio-astro-tools/casa-python>`_ that resolves
this issue by creating a ``~/.casa`` directory in which new packages can be
installed.

