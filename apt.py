# Handle data from APT.txt

from faddsdata.format_definitions import APT_RECORDS, ATT_RECORDS, RWY_RECORDS, RMK_RECORDS

def build_list_of_lengths(definition):
    """Take a SortedDict and iterate over it, building a list of field lengths."""
    lengths = []
    for key in definition:
        lengths.append(definition[key])
    return lengths

def calculate_lengths(fields):
    count = 0
    out = []
    for i in fields:
        end = 0
        for x in range(0, count):
            end += fields[x]
        if end != 0:
            out.append(end)
        count += 1
    return out

# calculate cumulative length from the list of lengths
APT_RECORD_LENGTHS = calculate_lengths(build_list_of_lengths(APT_RECORDS))
ATT_RECORD_LENGTHS = calculate_lengths(build_list_of_lengths(ATT_RECORDS))
RWY_RECORD_LENGTHS = calculate_lengths(build_list_of_lengths(RWY_RECORDS))
RMK_RECORD_LENGTHS = calculate_lengths(build_list_of_lengths(RMK_RECORDS))

# borrowed from http://code.activestate.com/recipes/65224/
def split_at(theline, cuts, lastfield=True):
    pieces = [ theline[i:j] for i, j in zip([0]+cuts, cuts) ]
    if lastfield:
        pieces.append(theline[cuts[-1]:])
    return pieces

def correlate(data, definition):
    combined = {}
    count = 0
    for key in definition.keys():
        combined[key] = data[count]
        count += 1
    return combined

if __name__ == '__main__':
    path = '/Users/afast/Downloads/56DySubscription_November_18__2010_-_January_13__2011/'
    raw = open(path + 'APT.txt')

    for line in raw:
        if line[:3] == 'APT':
            val = correlate(split_at(line, APT_RECORD_LENGTHS), APT_RECORDS)
        elif line[:3] == 'ATT':
            val = correlate(split_at(line, ATT_RECORD_LENGTHS), ATT_RECORDS)
        elif line[:3] == 'RWY':
            val = correlate(split_at(line, RWY_RECORD_LENGTHS), RWY_RECORDS)
        elif line[:3] == 'RMK':
            val = correlate(split_at(line, RMK_RECORD_LENGTHS), RMK_RECORDS)
        import pdb; pdb.set_trace()
