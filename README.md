# Heartbeat

## Here's a question: Can we tell a normal heartbeat from an abnormal one?
In other words, can we analyze audio recordings of heartbeats, with all their variation as well as environmental noise and still be able to distinguish between normal heartbeat from one where you should call an ambulance?

And, from there, can we develop a tool that allows people in less well served locations to maximize their chance of survival by getting them to healthcare sooner.


## So, Why Am I Interested In This?

* I'm a former paramedic and I've been on calls where people would have benefitted from something like this, both in terms improving mortality and morbidity.

* I like hard problems that are worthwhile and I know that medicine has been trying to crack this problem for about 50 years now.

* This seemed like and this seemed like something that hadn't been done before.

On that last point, well ... yes and no

... but mostly no.


## The Data - And It's Backstory 
One of the underpinnings of the not being able to classify heart rhythms by sound is that up until recently, there was no good set of audio recordings. In 1999 NIH funded MIT's Laboratory for Computational Physiology to establish and run [physionet](https://physionet.org/) as repository of recordings, models and research -- all open and freely available. Physionet also sponsors yearly challenges which are usually related to the heart; the dataset I used was from the [2016 Physionet heartsounds challenge](https://physionet.org/content/challenge-2016/1.0.0/).

The recordings were sourced from contributors around the world and were collected both clinical or nonclinical environments.  The Challenge training set consists of five databases (A through E) containing a total of 3,126 heart sound recordings, lasting from 5 seconds to just over 120 seconds. Of the recordings, about 1/2 are normal  

Physionet did an excellent job with structuring the recordings. They kept a separate holdout set for validation that was released only after the competition was concluded. The data researchers was pre-randomized, and split into five subsets, each with a separate files listing which recordings were normal and abnormal. More information on the datas as well as the results of the top models can be found at the [challenge website](https://physionet.org/content/challenge-2016/1.0.0/).


## A Bit On How The Heart Works

EKG https://www.sciencedirect.com/topics/medicine-and-dentistry/phonocardiography
PCG
PPG ppg.png (source: paulvangent.com)

Four locations are most often used to listen to the heart sounds, which are named according to the positions where the valves can be best heard:

* Aortic area - centered at the second right intercostal space.
* Pulmonic area - in the second intercostal space along the left sternal border.
* Tricuspid area - in the fourth intercostal space along the left sternal edge.
* Mitral area - at the cardiac apex, in the fifth intercostal space on the midclavicular line.

[![alt_text](image/path.png)](hyperlink)

The heart sound recordings were collected from different locations on the body. The typical four locations are aortic area, pulmonic area, tricuspid area and mitral area, but could be one of nine different locations. In both training and test sets, heart sound recordings were divided into two types: normal and abnormal heart sound recordings. The normal recordings were from healthy subjects and the abnormal ones were from patients with a confirmed cardiac diagnosis.



## Prior Work
As I mentioned, people have been trying to solve this for the last 50 or so years. Some of the prior work includes

Artificial neural networks (ANNs) have been the most widely used machine learning-based approach for heart sound classification. Typical relevant studies grouped by the signal features as the input to the ANN classifier include: using wavelet features [12], time, frequency and complexity-based features [13], and time-frequency features [14]. A number of researchers have also applied support vector machines (SVM) for heart sound classification in recent years. The studies can also be divided according to the feature extraction methods, including wavelet [15], time, frequency and time-frequency feature-based classifiers [16]. Hidden Markov models (HMM) have also been employed for pathology classification in PCG recordings [17,18]. Clustering-based classifiers, typically the k-nearest neighbors (kNN) algorithm [19,20], have also been employed to classify pathology in PGCs. In addition, many other techniques have been applied, including threshold-based methods, decision trees [21], discriminant function analysis [22,23] and logistic regression.


## Process

[![alt_text](image/path.png)](hyperlink)

[![](images/logos.png)](developer.spotify.com)


## Where All The Freqs?


## Resources
http://www.paulvangent.com -- work was with a PPG but well written and interesting
