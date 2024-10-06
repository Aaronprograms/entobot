import sciolyid as bot

bot.setup(

    # required
    bot_description="Entomology ID - Troy High's SciOly Discord Bot for Ento Nerds,  # short bot description
    bot_signature="Entomology ID - A Bug Bot,  # signature for embeds
    prefixes=["e.", "E."],  # bot prefixes, primary prefix is first in list
    id_type="bug",  # star, fossil, muscle, etc. - singular noun
    github_image_repo_url=None,  # link to github image repo
    support_server=None,  # link to discord support server
    source_link=None,  # link to source code (may be hosted on github)

    # only required if id_groups is True
    category_name="taxon",  # space thing, bird order, muscle group - what you are splitting groups by

    # optional
    name="ento-id",  # all lowercase, no spaces, doesn't really matter what this is
    download_dir="image/",  # name of downloaded image directory (no trailing slash)
    data_dir="data/",  # directory of data lists (wiki, alias, id lists), with trailing slash
    list_dir="group",  # directory of id lists (no trailing slash)
    wikipedia_file="wikipedia.txt",  # name of wikipedia file
    alias_file="aliases.txt",  # name of alias file
    logs=True,  # enable logging
    log_dir="logs/",  # directory to put generated log files (no trailing slash)
    file_folder="bot_files",  # directory to put bot generated files (downloaded images/logs), can be empty string, no trailing slash
    invite="This bot is currently not avaliable outside the support server.",  # bot server invite link
    authors="Aaron",  # creator names
    id_groups=True,  # true/false - if you want to be able to select certain groups of items to id
    category_aliases={},  # aliases for categories
    disable_extensions=[],  # list of default extensions to disable
    custom_extensions=[],  # list of extensions to use
    sentry=True,  # enable sentry error monitoring
    local_redis=False,  # run a redis server locally, alternative is to use a redis url env. var
    bot_token_env="token",  # name of token env. var
    sentry_dsn_env="SENTRY_DISCORD_DSN",  # name of sentry env. var (only if sentry is True)
    redis_env="REDIS_URL",  # name of redis env. var (only if local_redis is False)

)

bot.start()
