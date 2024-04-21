# Pulse

## Overview

`pulse` is a utility that schedules the execution of shell commands.

`pulse` runs shell commands according to a user-defined schedule. The schedule is specified in the syntax `YYYY.MM.DD.hh.mm.ss`, where each field (year, month, day, minute, and second) can include a range (`[1-20]`), a list (`[2,3,5]`), or a catch-all operator (`*`) that will run on every value for that field.

## Usage

The command syntax follows the format: `pulse <schedule> "<command>"`

- `<schedule>`: The syntax `YYYY.MM.DD.hh.mm.ss` specifies the year, month, day, hour, minute, and second.
- `<command>`: The shell command to be executed.

The scheduling syntax allows for flexibility and includes the following elements:

Each year, month, day, minute, and second field may also contain a range (`[1-20]`), a list (`[2,3,5]`), or a catch-all operator (`*`).

## Examples

This will run the shell command `ls -al .` once on February 24, 2024, at 17:20:10:

`pulse 2024.02.24.17.20.10 "ls -al ."`

And this will run `ls -al .` every minute on the 22nd to 24th days of the 2nd and 5th month of 2024 at the 20th second:

`pulse 2024.[02,05].[22-24].*.20 "ls -al ."`

`pulse 2024.02.*.16.[5-9].[10,20] "ls -al ."`

## License

`pulse` is available under the MIT license
