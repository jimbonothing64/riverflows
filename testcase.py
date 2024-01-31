"""Generate test case"""

def nice_list(list, name, gap=10):
    output = f"{name} = [\n    "
    for i, time in enumerate(list):
        output += f'{time}, '
        if i % gap == gap-1:
            output += '\n    '
    output = output[:-2]
    output += '\n]'
    return output

def test_case(filename, days=None):
    times = []
    flows = []
    with open(filename) as infile:
        lines = infile.read().splitlines()
        for line in lines[1:]:
            _, datetime, flowrate = line.split(',')
            day = int(datetime[:2])
            if not days or day in days:
                times.append(int(datetime))
                flows.append(float(flowrate))
        
        
        time_str = nice_list(times, 'times')
        flow_str = nice_list(flows, 'flows', 7)

        print(time_str + '\n' + flow_str)
            
            


def main():
    test_case('dst/Riverflow_AvonOtakaroRiver_GloucesterStreetBridge.csv', [1])


main()