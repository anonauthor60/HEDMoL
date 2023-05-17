# Electron-Derived Molecular Representation Learning for Real-World Molecular Physics
Various representation learning methods for molecular structures have been devised to accelerate data-driven drug and materials discovery. However, the representation capabilities of existing methods are essentially limited to \textit{atom}-level information, which is not sufficient to describe real-world molecular physics. Although \textit{electron}-level information can provide fundamental knowledge about chemical compounds beyond the atom-level information, obtaining the electron-level information in real-world molecules is computationally impractical and sometimes infeasible. We proposes a new method for learning electron-derived molecular representations without additional computation costs by transferring pre-calculated electron-level information about small molecules to large molecules of our interest. The proposed method achieved state-of-the-art prediction accuracy on extensive benchmark datasets containing experimentally observed molecular physics.

# Before Execution
- Please check the ``requirements.txt`` file.
- If you want to use pre-processed ESOL, IGC50, and LC50 datasets, decompress the ``dataset.zip`` file in the ``save/dataset`` folder.
- We saved the prediction results of HEDMoL on the benchmark datasets in the ``save`` folder.

# Run
You can train and evaluate HEDMoL by executing ``train_eval.py``.
