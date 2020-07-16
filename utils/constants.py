UNIVARIATE_DATASET_NAMES = ['FiftyWords', 'Adiac', 'ArrowHead', 'Beef', 'BeetleFly', 'BirdChicken', 'Car', 'CBF',
                            'ChlorineConcentration', 'CinCECGTorso', 'Coffee',
                            'Computers', 'CricketX', 'CricketY', 'CricketZ', 'DiatomSizeReduction',
                            'DistalPhalanxOutlineAgeGroup', 'DistalPhalanxOutlineCorrect', 'DistalPhalanxTW',
                            'Earthquakes', 'ECG200', 'ECG5000', 'ECGFiveDays', 'ElectricDevices', 'FaceAll', 'FaceFour',
                            'FacesUCR', 'Fish', 'FordA', 'FordB', 'GunPoint', 'Ham', 'HandOutlines',
                            'Haptics', 'Herring', 'InlineSkate', 'InsectWingbeatSound', 'ItalyPowerDemand',
                            'LargeKitchenAppliances', 'Lightning2', 'Lightning7', 'Mallat', 'Meat', 'MedicalImages',
                            'MiddlePhalanxOutlineAgeGroup', 'MiddlePhalanxOutlineCorrect', 'MiddlePhalanxTW',
                            'MoteStrain', 'NonInvasiveFetalECGThorax1', 'NonInvasiveFetalECGThorax2', 'OliveOil',
                            'OSULeaf', 'PhalangesOutlinesCorrect', 'Phoneme', 'Plane', 'ProximalPhalanxOutlineAgeGroup',
                            'ProximalPhalanxOutlineCorrect', 'ProximalPhalanxTW', 'RefrigerationDevices',
                            'ScreenType', 'ShapeletSim', 'ShapesAll', 'SmallKitchenAppliances', 'SonyAIBORobotSurface1',
                            'SonyAIBORobotSurface2', 'StarLightCurves', 'Strawberry', 'SwedishLeaf', 'Symbols',
                            'SyntheticControl', 'ToeSegmentation1', 'ToeSegmentation2', 'Trace', 'TwoLeadECG',
                            'TwoPatterns', 'UWaveGestureLibraryAll', 'UWaveGestureLibraryX', 'UWaveGestureLibraryY',
                            'UWaveGestureLibraryZ', 'Wafer', 'Wine', 'WordSynonyms', 'Worms', 'WormsTwoClass', 'Yoga']

# UNIVARIATE_DATASET_NAMES = ['Meat', 'Coffee']

UNIVARIATE_ARCHIVE_NAMES = ['TSC', 'InlineSkateXPs', 'SITS']
UNIVARIATE_ARCHIVE_NAMES = ['TSC']

SITS_DATASETS = ['SatelliteFull_TRAIN_c301', 'SatelliteFull_TRAIN_c200', 'SatelliteFull_TRAIN_c451',
                 'SatelliteFull_TRAIN_c89', 'SatelliteFull_TRAIN_c677', 'SatelliteFull_TRAIN_c59',
                 'SatelliteFull_TRAIN_c133']

InlineSkateXPs_DATASETS = ['InlineSkate-32', 'InlineSkate-64', 'InlineSkate-128',
                           'InlineSkate-256', 'InlineSkate-512', 'InlineSkate-1024',
                           'InlineSkate-2048']

dataset_names_for_archive = {'TSC': UNIVARIATE_DATASET_NAMES,
                             'SITS': SITS_DATASETS,
                             'InlineSkateXPs': InlineSkateXPs_DATASETS}
