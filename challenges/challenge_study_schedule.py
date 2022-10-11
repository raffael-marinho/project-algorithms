def study_schedule(permanence_period, target_time):
    count = 0
    for hours in permanence_period:
        try:
            if hours[0] <= target_time <= hours[1] and target_time is not None:
                count += 1
        except TypeError:
            return None
    return count
