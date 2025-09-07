# Utility function to convert kebab-case to a human-readable string
def kebab_to_str(slug):
    return slug.replace('-', ' ').title()