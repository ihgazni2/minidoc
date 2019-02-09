======
ReadMe
======


Installation
------------
    ::
    
    $ pip3 install minidoc


License
-------

- MIT



Quickstart
----------
- pip3 install minidoc

- make a workdir, such as "TEST"
    
    ::
    
        mkdir TEST
        cd TEST
   
- edit your code.tst.py  as below:

    ::
        
        cat code.tst.py
        

.. image:: /docs/images/code.tst.py.00.png

- run cmd **minidoc** ,
  will auto exec the code in code.tst.py, 
  and auto save  the terminal screen-shot(or recording)
  
  ::
      
      minidoc
      tree
      TEST# tree
      .
      ├── code.tst.py
      ├── images------------------------------->generated svgs
      │   ├── __getitem__.1.svg
      │   └── __init__.0.svg
      └── Usage.rst---------------------------->generated .rst
      
      1 directory, 4 files
      TEST#

      
.. image:: /docs/images/code.tst.py.1.png
.. image:: /docs/images/code.tst.py.2.png
.. image:: /docs/images/code.tst.py.3.png


- minidoc -h

    ::
        
        TEST# minidoc -h
        usage: minidoc [-h] [-tst TEST_FILE] [-codec CODEC] [-still STILL_FRAMES]
                       [-rows ROWNUMS] [-dst DST_DIR] [-title TITLE] [-tbot TITLE_BOT]
                       [-ebot ENTRY_BOT]
        
        optional arguments:
          -h,                   --help                       show this help message and exit
          -tst    TEST_FILE,    --test_file TEST_FILE        .tst.py file name
          -codec  CODEC,        --codec CODEC                .tst.py file codec
          -still  STILL_FRAMES, --still_frames STILL_FRAMES  generate screen shot
          -rows   ROWNUMS,      --rownums ROWNUMS            screen height
          -dst    DST_DIR,      --dst_dir DST_DIR            destination svg dir
          -title  TITLE,        --title TITLE                parent title
          -tbot   TITLE_BOT,    --title_bot TITLE_BOT        parent title bottom char
          -ebot   ENTRY_BOT,    --entry_bot ENTRY_BOT        entry title bottom char


Usage
-----

- from code

    ::
        
            

- from cmdline

    ::

        root@# minidoc code.rst.py wkdir
        root@# tree wkdir

Features
--------

- auto generate .rst doc from .tst.py
- auto exec test-code in .tst.py 
- auto record the screen and save as .svg


References
----------

* termtosvg
* elist
* efdir
* estring
