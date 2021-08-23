# hamilton - static site generator

> "Legacy, what is a legacy? It's planting seeds in a garden you never get to see."
> - Lin Manuel Miranda, *The World Was Wide Enough*

A static site generator. Forked from [AutoSite Legacy](https://github.com/dotcomboom/AutoSite-Legacy).

The goal of hamilton is to be a fully-featured successor to AutoSite Legacy while incorporating some features of Apricot (the new AutoSite build engine) and some features I had previously coded as plugins.

## Roadmap

 - [X] Rebrand from "AutoSite" to "hamilton" throughout
    - [X] Maybe refactor code slightly?
        - The original AutoSite (Legacy) was written as a Python script and then shoved into a main() function. Maybe split some parts out into their own functions?
 - [X] Re-implement some Apricot features
    - [X] `#modified#` - Modified date, automatically generated from the file's modtime if not manually provided
        - Why not?
    - [X] Attributes are processed twice, once on the template itself and again following conditionals being replaced
        - Not sure why this is done, but why not?
    - [X] Non-existant template defaults to `default` template rather than creating a *new* template from the original default
    - [X] `in/` renamed to `pages/`
        - Just makes sense.
 - [ ] Implement some QoL features
    - [ ] Nested/multiline conditionals if I can get them working
        - Would be a lot easier to mess around with and make the generated result look presentable
    - [ ] Add a way to escape attributes
        - For ease of documentation, mainly
        - dcb actually [did take a pass at implementing this](https://dotcomboom.somnolescent.net/patio/2020/04/03/autosite-devlog-5-rc3-progress-update/), but the initial pass at it ended up breaking a PHP site of his that used it (not sure why he used it for a PHP page but whatever) so he removed it.
            - Find a way to do it that doesn't break with PHP?
    - [ ] Config file
        - Allows defining attributes globally that can be overwritten in specific cases
        - Also can be used for other build vars such as `baseurl` (for `#cleanurl#`, see below)
    - [ ] Restructure how plugins work
        - AutoSite Legacy implements plugins as basically just scripts that get ran inside the parsing of the file
            - Nothing's wrong with this, but it could be handled more efficiently
        - New plugins register functions at three stages:
            - 1. Pre-processor, runs on the content after it gets massaged into HTML but before it gets substituted into the template
            - 2. Blocktag (see below)
            - 3. Post-processor, runs on the final product before it gets written to the file
 - [ ] Implement some new features that I previously coded as plugins
    - [ ] `#cleanurl#` - a clean URL for the page which doesn't include `index.html` if it exists at the end of the path
        - generates cleaner URLs for opengraph
        - basically `baseurl+path`, with the aforementioned if-case to remove index.html from the end
        - requires the config file (see above) to define `baseurl`.
            - alternatively, for a config-less solution that could be implemented in AutoSite proper, have a `[#cleanpath#]` that can be slapped after a base URL on the template side of things
    - [ ] Unsee/Unpublish - prevents a file in `pages/` from generating a file in `out/`
        - basically just nope out of file generation if `"unpublish" in attribs and attribs["unpublish"][0].lower() not in ('n','f')`
            - `('n','f')` for "no" and "false"
        - the plugin version couldn't nope out of file generation so instead it just overwrote the `template` var with an error page
            - kept people from accessing a page they shouldn't be able to see but they could still tell it existed
    - [ ] Blocktags - like attributes, but with extra scripting
        - i implemented an entire system for this in a plugin despite only using it once (for navigation links in a fanfiction site)
            - could be useful in other cases?
        - preferably implemented as part of the plugin restructure (see above)
        - by implementing this at the base level, avoid having to reinitialize the blocktag plugins every time a new page is being rendered
            - also, if paired with the plugin restructure, this benefit will extend to all plugins of any type
