## Didi data: setup

### Requirements

[Install git-lfs](https://github.com/git-lfs/git-lfs/wiki/Installation)

### Structure

```release2/ \
  Data-points-processed/
   1/
    bag_name/
     lidar/...
     tracklet_labels.xml => as output from bag_to_kitti.py
     tracklet_labels_trainable.xml => this one is fine-tuned
   2/
    bag_names/...
   3/
    bag_names/...
   test/
    ...
  release3/
```

### Considerations

XML tracklets are referenced by LIDAR frames (not camera frames), and they are expected to be loaded and read using the Diditracklet class, which has methods to load the tracklet and then load the lidar data along with the bounding box.

Since there are frames where the aligning algorithm wasn't sure if it aligned correctly, the XML tracklet has a per-frame `<state>` attribute that is marked as 0 if we are unsure about the quality of the pose at that given frame (it happens in very few frames but still).

You are supposed to use `tracklet_labels_trainable.xml` as these have the best quality.

The XML have the obstacle dimensions as given by the organization. I checked all 3 cars used in round 1 (release 2) and the car dimensions provided are SMALLER than the manufacturer advertised dimensions. If you want to extract points that belong to an obstacle it's probably a good idea to make the bounding box a bit bigger to make sure you do not miss any points.
