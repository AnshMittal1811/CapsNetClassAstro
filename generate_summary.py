import h5py
import cv2
import os
import os.path as osp
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str, required=True, help="path to h5 result file")

def frm2video(frm_dir, summary, vid_writer):
    print('summary', summary)
    for idx, val in enumerate(summary):
        if val == 1:
            # here frame name starts with '000001.jpg'
            # change according to your need
            frm_name = str(idx+1).zfill(6) + '.jpg'
            print(frm_name)
            frm_path = osp.join(frm_dir, frm_name)
            frm = cv2.imread(frm_path)
            frm = cv2.resize(frm, (args.width, args.height))
            vid_writer.write(frm)

def get_summary(model, )
    with torch.no_grad():
        #model.eval()

        cps = dataset[key]['change_points'][...]
        num_frames = dataset[key]['n_frames'][()]
        nfps = dataset[key]['n_frame_per_seg'][...].tolist()
        positions = dataset[key]['picks'][...]
        user_summary = dataset[key]['user_summary'][...]

        machine_summary = vsum_tools.generate_summary(probs, cps, num_frames, nfps, positions)
        print('machine_summary', machine_summary)
