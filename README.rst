Vanilla forum - Community forums evolved
========================================

`Vanilla`_ allows you to create a customized community that rewards
positive participation, automatically curates content and lets members
drive moderation. We believe that online communities should be unique,
intuitive and engaging.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Vanilla configurations:
   
   - Installed from upstream source code to /var/www/vanilla

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, Adminer: username **root**
-  Vanilla: username **admin**


.. _Vanilla: http://vanillaforums.org/
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _Adminer: http://www.adminer.org/
