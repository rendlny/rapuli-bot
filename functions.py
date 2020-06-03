#takes in a string and returns correct integer for that pattern
def turnipPatternToInt(pattern):
    pattern = pattern.lower()

    #possible pattern names enter by user
    idk_list = ["idk", "i-dont-know", "unknown"]
    fluctuating_list = ["fluctuating", "random"]
    small_list = ["small", "small-spike"]
    large_list = ["large", "large-spike", "big", "big-spike"]
    decreasing_list = ["decreasing", "lowering"]

    if pattern in idk_list:
        return ''

    if pattern in fluctuating_list:
        return 0

    if pattern in small_list:
        return 3

    if pattern in large_list:
        return 1

    if pattern in decreasing_list:
        return 2

def addUsersTurnipPriceToMsg(user, msg, price):
    #check if user posting their price is already mentioned in the pinned msg
    if ctx.message.author.mention in pin_content:
        msg_parts = msg.split("|")
    else:
        new_pinned_msg = msg+"\n\n| "+user+" => https://turnipprophet.io/?prices="+price+"."
    return new_pinned_msg
