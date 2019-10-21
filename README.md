# ***acPDRP***
***acPDRP***, a predictor of multiple features in protein disordered regions ,was trained and tested by Uniprot90 and evaluated by CASP9 and CASP10 datasets.
The results of four evaluation indexes including **Precision**, **Bacc**, **MCC** and **AUC** in two datasets of CASP9 and CASP10 are better than ***[DeepCNF-D](https://www.mdpi.com/1422-0067/16/8/17315/htm)*** and the related methods mentioned.  
  
  
![image](https://github.com/ShoupengHe314/Depository/blob/master/Pictures/ac_p1.jpg)



## News
- 20/10/2019: Upload the script and the predicted model for the first time and test if it is available


## Get started


### Environment Requires

- [Anaconda 3.7 for Windows](https://repo.anaconda.com/archive/Anaconda3-2019.10-Windows-x86_64.exe)  
- [Anaconda 3.7 for macOS](https://repo.anaconda.com/archive/Anaconda3-2019.10-MacOSX-x86_64.pkg)  
- [Anaconda 3.7 for Linux](https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh)  

### Install
Download and install Anaconda 3.7 you need, and put *acPDRP.py* into the installed Anaconda path:Anaconda3\Lib\site-packages.


### Using
You can python the script called *predict_test.py* and the input file is your protein sequence the output file are the predicted results.

```
python predict_test.py <Input File> <Output File>
```


### Input File
The input file must be a protein sequence and format in FASTA. In view of the protein sequence requirements of ***[DISPHOS 1.3](http://www.dabi.temple.edu/disphos/)*** for protein phosphorylation site prediction, the minimal length of the protein sequence is limited to **25** residues and the maximal one is limited to **5000** residues.  
The FASTA sequence seems like below:
```
>test_sequence
IMWRNAKRQSDRFYDEDVFINGEGLEPEQDTRGVDNAHMVTNHHALRSRDNIYEYRDSPSTKTLASKAHTDTTSLRSPSSLAMTQKSSSQASLKSGISLKETNGHLVKQSERAATPRSQQNGSIAKVASPPVEEKRLLQPLSSTPVTQLQAEPAKRVPTAASVSGSSRSTTPVPSARSTTTHTTTATLSSQPAAQPRRTHLVEGVPQTSVHHHHHH
```

### Output Files
The first line is sequence name and the second line is predicted result. You can get the original predicted score or set the threshold to get the intuitive predicted label.
The time-consuming of getting the prediction results is related to the length of the input protein sequence. The longer the length is, the longer the time-consuming is.  
The output file seems like below:

#### Output score
```
>test_sequence_score
0.97, 0.985, 0.9833, 0.98, 0.98, 0.9725, 0.97, 0.96, 0.9625, 0.965, 0.965, 0.965, 0.97, 0.975, 0.9825, 0.9875, 0.96, 0.9425, 0.9425, 0.95, 0.9775, 0.9825, 0.98, 0.975, 0.965, 0.975, 0.9775, 0.9875, 0.995, 0.985, 0.975, 0.975, 0.975, 0.98, 0.98, 0.9725, 0.97, 0.965, 0.9725, 0.9775, 0.98, 0.99, 0.9825, 0.95, 0.95, 0.93, 0.93, 0.9625, 0.9625, 0.975, 0.965, 0.9475, 0.94, 0.935, 0.95, 0.965, 0.9625, 0.975, 0.9725, 0.9725, 0.9825, 0.97, 0.945, 0.945, 0.94, 0.95, 0.9725, 0.9675, 0.9725, 0.965, 0.9625, 0.9625, 0.95, 0.945, 0.9425, 0.9375, 0.945, 0.9575, 0.9725, 0.96, 0.955, 0.9575, 0.955, 0.9725, 0.9825, 0.985, 0.9825, 0.9925, 0.99, 0.9775, 0.9825, 0.9675, 0.955, 0.9575, 0.94, 0.92, 0.93, 0.94, 0.955, 0.9875, 0.985, 0.975, 0.97, 0.9575, 0.95, 0.9525, 0.955, 0.955, 0.9675, 0.97, 0.9725, 0.98, 0.9775, 0.975, 0.975, 0.9775, 0.9825, 0.99, 0.99, 0.9875, 0.9675, 0.945, 0.935, 0.94, 0.9525, 0.965, 0.9675, 0.965, 0.965, 0.965, 0.9675, 0.9675, 0.9675, 0.9775, 0.9775, 0.97, 0.9725, 0.94, 0.9425, 0.9525, 0.945, 0.97, 0.94, 0.93, 0.9375, 0.92, 0.9525, 0.95, 0.955, 0.9675, 0.94, 0.9425, 0.9425, 0.95, 0.965, 0.9675, 0.96, 0.9625, 0.975, 0.96, 0.9275, 0.9, 0.84, 0.8575, 0.89, 0.915, 0.9675, 0.9625, 0.9675, 0.96, 0.9675, 0.9425, 0.94, 0.95, 0.94, 0.975, 0.965, 0.9575, 0.965, 0.965, 0.975, 0.9825, 0.98, 0.975, 0.96, 0.94, 0.945, 0.945, 0.965, 0.9775, 0.9775, 0.9775, 0.98, 0.9825, 0.98, 0.985, 0.9775, 0.9825, 0.97, 0.96, 0.9575, 0.8925, 0.8775, 0.8775, 0.885, 0.945, 0.97, 0.965, 0.965, 0.9675, 0.9725, 0.985, 0.985, 0.9867, 0.985, 0.99
```

#### Output label
```
>test_sequence_label
111111111111111110011111111111111111111111111001111000111111110001111111100001111111111111111100001111111111111111111111100011111111111110010100001111000111111100000011111001011111111110001111111111111000001111111111
```
## References
Wu C , Chen J , Liu Y , et al. Improved Prediction of Regulatory Element Using Hybrid Abelian Complexity Features with DNA Sequences[J]. International Journal of Molecular Sciences, 2019, 20(7).

Wang, Sheng, Weng, et al. IJMS, Vol. 16, Pages 17315-17330: DeepCNF-D: Predicting Protein Order/Disorder Regions by Weighted Deep Convolutional Neural Fields[J]. 2015.

Iakoucheva LM, Radivojac P, Brown CJ, O'Connor TR, Sikes JG, Obradovic Z, Dunker AK. Intrinsic disorder and protein phosphorylation. Nucleic Acids Research, 2004, 32 (3), 1037-1049.

## Contact us
huxuehai@mail.hzau.edu.cn (E-mail can be in Chinese)  
sp_he@webmail.hzau.edu.cn (E-mail can be in Chinese)  
