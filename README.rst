Introduction
============

Have you wondered how many times certain packages were downloaded from pypi
during their lifetime? or how well are your packages doing?

Well you can use vanity_ but then you have to get every package name you
want to check or you can use this package.

Command line usage
-------------------

::

    $ python counter.py name=kotti
    bobtemplates.kotti : 264 downloads last_month:
    Kotti : 6324 downloads last_month:
    kotti_accounts : 378 downloads last_month:
    kotti_analytics : 93 downloads last_month:
    kotti_blog : 373 downloads last_month:
    kotti_calendar : 403 downloads last_month:
    kotti_contactform : 575 downloads last_month:
    kotti_contentpreview : 139 downloads last_month:
    ...

Valid keys for search are:
- name
- version
- author
- author_email
- maintainer
- maintainer_email
- home_page
- license
- summary
- description
- keywords
- platform
- download_url

Invalid keys are ignored.
