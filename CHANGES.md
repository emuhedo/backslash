# Changelog

## Version 2.12.5

* Fixed incorrect previous fix to metadata display

## Version 2.12.4

* Increased gunicorn worker timeout to handle long queries

## Version 2.12.3

* Fix URL display and links in metadata listings
* Fix handling of "status" query for sessions, including an issue where the search was case-sensitive
* Increased default query timeout to 60 seconds

## Version 2.12.1

* Fixes a bug in error rendering

## Version 2.12.0

* Backslash now supports reporting interruption exceptions to help determine what caused the session to be interrupted. When the sessions are reported with a compatible toolchain (for example, Slash >= 1.5.0), the session and test views will show the interruption exceptions and their contexts
* Added an option to display metadata values in an accessible location for tests and sessions
* Warnings are now deduplicated within sessions and tests, preventing DB bloat
* Added a view for test cases. This is planned to evolve into a suite management feature over the next releases
* Fixed the order of display of quick-jump items, and they are now sorted by name
* Added the ability to search by product type
* Added a "status_description" field for tests, allowing setting more informative information on what the test is currently doing (via API)
* Added timing metrics API, enabling tests and sessions to display the total time distribution spent while running
* Fixed indication of search term syntax errors

## Version 2.11.1

* Fixed handling of test timespan when the test starts and before a keepalive is received

## Version 2.11.0

* Added search option to user view
* Added support for discarding sessions. Admins can now mark sessions for deletion after a certain period of time (30 days by default). This is useful for temporary sessions that are not interesting for keeping forever.
* Sessions can have a TTL, automatically marking their discard date on keepalives and session ends
* Support reporting of remote and local SCM branches
* Removed the "mark archived" and "mark investigated" features. Investigation will be added in a future release as a part of a stricter workflow, and archiving can now be replaced with discarding sessions

## Version 2.10.0

* Added pagination navigation to session and test error views
* Improved navigation when examining parallel sessions
* Pressing 'u' when inside a test will take you back to the session test list
* Misc. bug fixes

## Version 2.9.0

* Time searches with 'at' are now more accurate, and can distinguish between searching for exact times and loose dates
* Added support for marking sessions as "terminated by fatal errors"
* Improvements to parallel runs display
* You can now search by ``test_info_id``, "previous executions" now lead to test search screen
* Added "Display" filter dropdown to test search view
* When no search results are found, Backslash now emits a descriptive message indicating it
* Minor UI fixes for searching


## Version 2.8.2

* Dramatically improved the performance of searching for previous executions of a test

## Version 2.8.0

* Favicon now displays an error/success icon for sessions and tests
* Initial support for parallel runs
* Add option to configure auxiliary services for supporting custom APIs
* Added documentation for installation, deployment and configuration (See https://backslash.readthedocs.org)
* *NOTE*: It is recommended to run Slash 1.2.4 or above with this release, to avoid a bug involving test counts and interactive sessions

## Version 2.7.0

* You can now search for sessions by contained test name via the `test = my_test_name` search clause
* You can now jump to the "last" page in the session tests view
* Added monitoring compatible with Prometheus (both natively via `/metrics` and the postgres exporter on port 9187)
* Tracebacks and errors are significantly improved, and now support collapsing of `self` attributes, copying the full exception to the clipboard and more
* Backslash now supports a newer way of uploading tracebacks via streaming uploads, improving performance on large tracebacks
* You can now search for sessions by status
* Deployment moved to Docker, ditched Ansible

## Version 2.6.3

* Many small UI/UX fixes and tweaks

## Version 2.6.0

* Support test parameters display for parameetrized tests
* Session information sidebar in session view is now collapsible, giving more room to examine tracebacks or exceptions
* Backslash now properly handles interrupted tests and sessions
* Add ability to search by product version
* Add option to control the landing page (all sessions/my sessions)
* Add session breakdown info to left information bar
* Add option to quickly expand side information bars for sessions
* Backslash now documents test indices
* J/K in test view jumps to next/previous test
* Comments can now be edited and deleted
* Comments now support markdown syntax for formatting

## Version 2.5.0

* Proxy users can now run sessions for emails that do not exist yet. This will create stub user records to be populated later
* Added session search
* Misc. performance improvements

## Version 2.4.0

* Support session labels, added through API

## Version 2.3.3

* Times are humanized by default again (accidental regression)

## Version 2.3.2

* Minor bug fixes

## Version 2.3.1

* Minor bug fixes

## Version 2.3.0

* Added basic support for searching tests and sessions using a query syntax
* Session view now displays durations
* Sessions and tests now have a preview of the latest comment made on them, when you hover over them. You can also hit `c` to toggle showing the latest comment on all items in view
* Many bugs fixed
  * Status display for tests inside abandoned sessions

## Version 2.2.0

* Major overhaul of UI
   * Session and test details are now nested views
   * Clearer flow between session, session errors/warnings, single tests and test errors/warnings
   * Simpler browsing of error details
   * Clearer indication of test/session statuses via status icons
* Many bugfixes and small improvements


## Version 2.1.0

* Added LDAP support
* Added initial setup wizard
* Added support for test parametrization info
* Added quick-jump to go to test subjects, users or test/session ids
* Added a user preferences mechanism for controlling various options, starting with the time format display
* Many bugfixes and small improvements

## Version 2.0.0

* First official release
