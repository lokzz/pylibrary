import time

class time_clc:
    def __init__(self, name = "", speak_on_start: bool = False, 
                start_fmt: str = '[{name}]\n',
                result_fmt: str = '[{name}] took {time_elapsed}s\n',
                checkpoint_fmt: str | None = '[{name} > {point_name} ({point_num})] took {time_point_elapsed}s since last checkpoint\n'
                ):
        self.startt = time.time()
        self.ckptimes = [self.startt]
        self.ckp_num = 0
        self.name = name
        self.start_fmt = start_fmt
        self.result_fmt = result_fmt
        self.checkpoint_fmt = checkpoint_fmt or self.result_fmt
        if speak_on_start: print(self.start_fmt.format(name=self.name), end='', flush=self.start_fmt.endswith('\n'))
    
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): self.end()

    def checkpoint(self, name: str, checkpoint_fmt: str | None = None):
        current_time = time.time()
        true_checkpoint = checkpoint_fmt or self.checkpoint_fmt
        time_elapsed = current_time - self.ckptimes[self.ckp_num]
        self.ckp_num += 1
        self.ckptimes.append(current_time)
        self.cur_cpkt_data = {"name": self.name, "point_name": name, "point_num": self.ckp_num, "time_point_elapsed": round(time_elapsed, 2), "time_elapsed": round(current_time - self.startt, 2)}
        print(true_checkpoint.format(**self.cur_cpkt_data), end='', flush=true_checkpoint.endswith('\n'))

    def end(self, result_fmt: str | None = None):
        self.endt = time.time()
        true_result = result_fmt or self.result_fmt
        self.time_elapsed = self.endt - self.startt
        self.data = {"name": self.name, "time_elapsed": round(self.time_elapsed, 2)}
        print(true_result.format(**self.data), end='', flush=self.result_fmt.endswith('\n'))