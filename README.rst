=====
flexi
=====




.. image:: https://pyup.io/repos/github/PythonCHB/flexi/shield.svg
     :target: https://pyup.io/repos/github/PythonCHB/flexi/
     :alt: Updates



Flexible hierarchical class structure built on dataclasses

Status
------

This package was originally built to support the needs of the ADIOS Oil Database project:

https://github.com/NOAA-ORR-ERD/adios_oil_database

It could be generally useful, so I've broken it out into its own package.

But at this point, it's not very feature complete or documented for general use.

If you want to really see it in action, see the ADIOS Oil Database project.

Goals
-----

The goal is to be able to create Python data models that enforce the structure of the data, but not the content. This supports "Messy" data, where you may want to be able to store and manipulate the data before it gets fixed up, if it ever does get fixed.

This system provides:

Serialization to/from JSON (or anything JSON compatible)

Optional Validation.

Optional "Clean up" -- automated code to manipulate the data to conform to some standard -- e.g./ a list of items should always be sorted.




Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
