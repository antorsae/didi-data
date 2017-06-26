import rosbag

part_secs = [       1495231988, 1495232018,
                    1495232061, 1495232089,
                    1495232194, 1495232261,
                    1495232469, 1495232538,
                    1495232667, 1495232753,
                    1495233254, 1495233294,
                    1495233362, 1495233539,
                    1495233567, 1495233615,
                    1495233690, 1495233704,
                    1495233938, 1495233999,
                    1495234133, 1495234184,
                    1495234207, 1495234258,
                    1495234261, 1495234293,
                    1495234298, 1495234302,
                    1495234311, 1495234333,
                    1495234336, 1495234338,
                    1495234391, 1495234404,
                    1495234407, 1495234415,
                    1495234426, 1495234427,
                    1495234566, 1495234590,
                    1495234593, 1495234610,
                    1495234613, 1495234662,
                    1495234676, 1495234682,
                    1495234687, 1495234704,
                    1495234710, 1495234764,
                    1495234774, 1495234782,
                    1495234785, 1495234788,
                    1495234891, 1495234996
                    ]

part_num = len(part_secs) / 2
print('{} parts to record'.format(part_num))

in_bag = rosbag.Bag('ped_train.bag')

part_no = -1
out_bag = None
for topic, msg, t in in_bag.read_messages():
    if part_no < 0 or t.secs > end:
        if out_bag:
            out_bag.close()
        if part_no < part_num - 1:
            part_no += 1
        else:
            print('finished processing parts')
            break

        start, end = part_secs[part_no*2], part_secs[part_no*2+1]
        assert start < end

        out_bag = rosbag.Bag('ped_train_{}_{}_{}.bag'.format(part_no, start, end), 'w')
        print('writing part {} - {} ...'.format(start, end))

    if t.secs > start:
        out_bag.write(topic, msg, t)

if out_bag:
    out_bag.close()
print('done')
