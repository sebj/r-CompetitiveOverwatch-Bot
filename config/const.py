subreddit = "competitiveoverwatch"
key_color = "#545452" # Reddit's "dark grey"
spoilers_enabled = False

user_agent = "r/" + subreddit + " sidebar updater. (Contact us via r/" + subreddit + " modmail)"

# Doubled from 5,120 to 10,240 in August '16
# https://www.reddit.com/r/changelog/comments/4x91ql/reddit_change_updates_to_the_sidebar/
sidebar_length_limit = 10_240

### Sidebar formatting

## Megathread
sidebar_replacement_megathreads = "{{MEGATHREADS}}"
format_megathread = "> [{}]({})\n"

## Event
sidebar_replacement_events = "{{EVENTS}}"
format_event = "####[{}{}]({}){}\n\n{}\n\n"

format_event_live = "**LIVE:** "

# Add commas to prizepool integer
format_event_prizepool = "\n\n${:,} Prize Pool"

# Event dates
format_event_date_line = "**{} – {}**"

format_event_date_tba = "Dates TBA"
format_event_date_started = "Ongoing"
format_event_date_same_month = "%d"
format_event_date = "%B %d"