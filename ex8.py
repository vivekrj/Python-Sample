Display = "%r %r %r %r"

print Display % (1, 2, 3, 4)
print Display % ("one", "two", "three", "four")
print Display % (True, False, False, True)
print Display % (Display, Display, Display, Display)
print Display % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
