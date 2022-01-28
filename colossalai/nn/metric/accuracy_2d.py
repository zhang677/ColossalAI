import torch
from colossalai.nn.layer.parallel_2d import reduce_by_batch_2d
from torch import nn

from ._utils import calc_acc


class Accuracy2D(nn.Module):
    """Accuracy for 2D parallelism
    """
    def __init__(self):
        super().__init__()

    def forward(self, logits, targets):
        """Calculate the accuracy of predicted labels.

        :param logits: Predicted labels
        :param targets: True labels from data
        """
        with torch.no_grad():
            correct = calc_acc(logits, targets)
            correct = reduce_by_batch_2d.apply(correct)
        return correct