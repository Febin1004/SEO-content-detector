def get_quality_label(word_count, readability):
    if (word_count > 1500) and (50 <= readability <= 70):
        return "High"
    if (word_count < 500) or (readability < 30):
        return "Low"
    return "Medium"
