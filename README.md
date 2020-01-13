## Spoiler Sensitive Video Summarization

With the plethora of video content uploaded to the internet each day, the amount of watchable content far exceeds the amount of time available for us to consume this visual content. That being said, the aim of  this research is not to create something that does the watching for us and merely generates a short summary; instead,  the aim of this project is to help us choose to watch which videos that we would enjoy the most  while preserving the viewing-integrity of the original video. In other words, we wish to be able  to generate preview video summaries that do not any essential plot items. To accomplish this task,  we developed an algorithm that is able to select a fraction of a video’s total frames to create a video  trailer/summary while excluding important frames that would detract from the main viewing experience  (i.e. it does not include any main plot points, spoilers, plot twists, etc.). This output video  would allow us to decide better whether we are interested in a particular video, and at the same time will still allows us to fully enjoy the video if we do choose to watch it since we will have avoided any spoilers.

## Poster
More details regarding the work can be found here: [Poster](https://github.com/mayank26saxena/spoiler-sensitive-video-summarization/blob/master/assets/poster.pdf)


## Dataset 
We used the following preprocessed dataset available at: [http://www.eecs.qmul.ac.uk/~kz303/vsumm-reinforce/datasets.tar.gz](http://www.eecs.qmul.ac.uk/~kz303/vsumm-reinforce/datasets.tar.gz) for building our model. 

## Reward Function
<img src="https://github.com/mayank26saxena/spoiler-sensitive-video-summarization/blob/master/assets/model.png" align="middle" width="768">
<img src="https://github.com/mayank26saxena/spoiler-sensitive-video-summarization/blob/master/assets/div-rep.png" width="512" align="middle">



## References
- [https://github.com/KaiyangZhou/pytorch-vsumm-reinforce](https://github.com/KaiyangZhou/pytorch-vsumm-reinforce)
