# CV for anomaly detection in industrial applications
[course google docs page](https://docs.google.com/document/d/1Kfa2MqIbNjHhnIZh8IsWokxnxm_1fJlOVxl7n_KqTJg/edit)

[Projects: expectations and grading](https://skoltech.instructure.com/courses/2471/discussion_topics/11936)
_______
## Project description 
Anomaly detection problems have a great importance in industrial applications, because anomalies usually represent faults, failures or the emergence of such. To detect these automatically, we propose deep learning algorithms for anomaly / fault detection and their classification. We develop an algorithm achieving
Segmentation
Defects classification
Its performance will be examined on two different problems: anomaly detection in oil pipelines and fault detection on transmission system components. Both these systems can span over thousands of kilometers, which makes manual inspection very costly. How such computer vision techniques can be applied on an industrial scale is discussed in the following.

The damage of pipelines that transport petroleum and gas products lead to serious environmental problems. Eliminating breakthroughs and their consequences is expensive. To avoid accidents, it is recommended to improve diagnostics quality and to increase the frequency of pipeline inspectors deployment. These are specialized robots (inspectors) that Identify defects and evaluate the thickness of the pipeline. Most of the techniques currently used for analysis relate to heuristical or traditional ML approaches and don’t involve CNN or DL algorithms.

Transmission infrastructure, on the other hand, physically connects power sources and consumers extending over thousands of kilometers. Many different components exist, which is why maintaining power grids is a serious cost factor for transmission system operators (TSOs). Automated fault detection could potentially help to decrease costs. To use an automated visual system however, specific infrastructure first needs to be identified and segmented, to then perform any type of fault detection. Therefore, the proposed deep learning-based approach, to segment and identify faulty components (i.e. insulators) in handheld footage, will be tested regarding its viability. If a deep-learning based approach would prove reliable, drones could monitor equipment automatically.
_______
## What makes it interesting/practical
Note that, once the insulator fails to work will cause the interruption of the entire transmission line or widespread power failure. To ensure the safe and reliable operation of the entire transmission line, it is necessary to check the transmission line insulators and find troubleshooting, if this is done with a fast approach this will prevent further failure of other components. Therefore, this project is not only interesting but can be used in practice by operators of power system grids. 
Moreover, regarding the pipeline defects detection problem we know about the interest of the biggest Russian oil and gas pipeline diagnostics company (Diaskan). They are currently working on applying ML to their diagnostics applications, and they have a particular interest in such algorithms. We have contacts with this company.
_______
## Datasets
- Problem 1: Real-world industrial data from one of the Russian oil companies. The data was collected from the pipeline inspectors. We have ground truth about defects and their location for data labeling. Overall we have 10 datasets for different pipes (thousands of meters long).  
- Problem 2: We need footage of electric infrastructure. Such footage is available in abundance on Youtube from people who ride trains. An excerpt from this video is decomposed into its frames. For the training datasets, a subset of frames obtained in (1) needs to be segmented manually to serve as ground-truth images.
_______
## References
- Problem 1:

[Journal "IEEE Transactions on Instrumentation and Measurement"](https://ieeexplore.ieee.org/xpl/aboutJournal.jsp?punumber=19)

1. [Defect Identification From MFL Images in Pipeline Inspection Using Convolutional Neural Network](https://ieeexplore.ieee.org/abstract/document/7878530?casa_token=v8fBoUaNFNsAAAAA:RGckea71AAcnLfNQe_vbXwjShEcaXELcaWurOf2P9RAzqycMb_RpU2A9gX09uAW-6KLIqpir-9tS4A)
2. [Machine Learning Techniques for the Analysis of Magnetic Flux Leakage Images in Pipeline Inspection](https://ieeexplore.ieee.org/document/5170224)
3. [Oil Pipeline Weld Defect Identification System Based on Convolutional Neural Network](http://itiis.org/digital-library/23389)
4. [Injurious or Noninjurious Defect Identification From MFL Images in Pipeline Inspection Using Convolutional Neural Network](https://ieeexplore.ieee.org/abstract/document/7878530?casa_token=v8fBoUaNFNsAAAAA:RGckea71AAcnLfNQe_vbXwjShEcaXELcaWurOf2P9RAzqycMb_RpU2A9gX09uAW-6KLIqpir-9tS4A)
5. [PhD thesis (Russian)](http://www.niiin.ru/upload/medialibrary/87d/87dab48dd2ec60910d4215fadbedcda6.pdf) (sorry for Russian)

- Problem 2:
1. http://downloads.hindawi.com/journals/mpe/2019/6397905.pdf
2. https://www.sciencedirect.com/science/article/abs/pii/S0263224119300831

